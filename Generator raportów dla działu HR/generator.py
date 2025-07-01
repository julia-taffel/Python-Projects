import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

# 1. Tworzenie raportów na dowolny okres czasu
# 2. Podsumowanie czasu pracy pracownika w danym przedziale czasowym
# 3. Wiele kontraktów w danym okresie, także okresy bez zatrudnienia.
# 4. Kontrakty mogą być na czas nieokreślony
# 5. Suma czasu pracy osobno dla odpowiednich kontraktów/okresów bez zatrudnienia.

# Cel: Ustalenie przedziałów czasowych, dla których czas pracy ma być zsumowany w raporcie

# Wynik: Posortowana lista przedziałów czasowych w strefie czasowej podanego przedziału raportu

def process_csv(file_csv, start, end, timezone = ZoneInfo("Europe/Warsaw")):
    data = pd.read_csv(file_csv, sep=";")
    
    #print(data.columns.tolist())
    data.rename(columns={
        "POCZĄTEK":"start_date",
        "KONIEC":"end_date"
    }, inplace=True)
    
    #Konwersja dat do zadanej strefy
    data["start_date"] =  pd.to_datetime(data["start_date"].str.strip(), format="mixed", utc=True).dt.tz_convert(timezone)
    data["end_date"] = pd.to_datetime(data["end_date"].str.strip(), format="mixed", errors="coerce", utc=True)
    data["end_date"] = data["end_date"].dt.tz_convert(timezone)
    
    #Data zakończenia raportu
    report_end_dt = datetime.fromisoformat(end).replace(tzinfo=timezone)
    data["end_date"] = data["end_date"].fillna(report_end_dt)
    
    #Data rozpoczęcia raportu
    report_start_dt = datetime.fromisoformat(start).replace(tzinfo=timezone)
    
    #Lista z przedziałami okresów pracy
    contracts = []
    for _, row in data.iterrows():
        interval_start = max(row["start_date"], report_start_dt)
        interval_end = min(row["end_date"], report_end_dt)
        if interval_start < interval_end:
            contracts.append((interval_start, interval_end))        
    
    contracts.sort()
    
    #Lista z przedziałami okresów bez zatrudnienia
    intervals = []
    if not contracts:
        intervals.append((report_start_dt, report_end_dt))
    else:
        if contracts[0][0] > report_start_dt: 
            intervals.append((report_start_dt, contracts[0][0]))
        
        for (prev_end, next_start) in zip([x[1] for x in contracts[:-1]], [x[0] for x in contracts[1:]]):
            if next_start > prev_end:
                intervals.append((prev_end, next_start))
                
        if contracts[-1][1] < report_end_dt:
            intervals.append((contracts[-1][1], report_end_dt))
    
    #Wszystkie przedziały razem
    everything = contracts + intervals
    everything.sort()
    
    #Zamiana dat na czytelne ISO8601
    result = [[a.isoformat(' '), b.isoformat(' ')] for a, b in everything]
    
    return result

#Wywołanie funkcji
result = process_csv(
    file_csv="example.csv", 
    start="2023-01-01T00:00:00", 
    end="2023-05-01T00:00:00"
    )

for interval in result:
    print(interval)