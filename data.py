```python
import pandas as pd

# 1. 하드코딩된 장치 및 지역 데이터 생성 및 CSV 저장
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "Device_Category": [
        "Desktop", "Mobile", "Tablet", "Mobile", "Desktop"] * 6,
    "Operating_System": [
        "Windows", "iOS", "Android", "iOS", "MacOS"] * 6,
    "Geolocation": [
        "USA", "South Korea", "Germany", "Japan", "Canada"] * 6,
    "Language": [
        "en-US", "ko-KR", "de-DE", "ja-JP", "fr-CA"] * 6,
}

# 데이터프레임 생성 및 CSV 저장
csv_filename = "device_geolocation_data.csv"
device_geolocation_data = pd.DataFrame(data)
device_geolocation_data.to_csv(csv_filename, index=False)

print(f"CSV 파일 '{csv_filename}' 저장 완료!")
```
