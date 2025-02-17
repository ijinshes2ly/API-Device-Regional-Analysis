```python
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
csv_filename = "user_behavior_data.csv"
user_behavior_data = pd.read_csv(csv_filename)

# 주요 지표 계산
avg_bounce_rate = round(user_behavior_data["Bounce_Rate"].mean(), 2)
avg_session_duration = round(user_behavior_data["Average_Session_Duration"].mean(), 2)

# 랜딩 페이지별 평균 이탈률 계산
landing_page_bounce_summary = user_behavior_data.groupby("Landing_Page")["Bounce_Rate"].mean().reset_index()

# 종료 페이지별 방문 횟수 계산
exit_page_summary = user_behavior_data.groupby("Exit_Page").size().reset_index(name="Exit_Count")

# 주요 지표 출력
summary_metrics = {
    "Average Bounce Rate (%)": avg_bounce_rate,
    "Average Session Duration (seconds)": avg_session_duration
}

summary_df = pd.DataFrame([summary_metrics])

# 데이터 시각화
# 랜딩 페이지별 평균 이탈률 시각화
plt.figure(figsize=(8, 5))
plt.bar(landing_page_bounce_summary["Landing_Page"], landing_page_bounce_summary["Bounce_Rate"],
        color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Landing Page")
plt.ylabel("Average Bounce Rate (%)")
plt.title("Average Bounce Rate by Landing Page")
plt.grid(axis='y')
plt.show()

# 종료 페이지별 방문 횟수 시각화
plt.figure(figsize=(8, 5))
plt.bar(exit_page_summary["Exit_Page"], exit_page_summary["Exit_Count"],
        color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Exit Page")
plt.ylabel("Exit Count")
plt.title("Exit Count by Page")
plt.grid(axis='y')
plt.show()

# 주요 분석 결과 출력
print("\n랜딩 페이지별 평균 이탈률:")
print(landing_page_bounce_summary)

print("\n종료 페이지별 방문 횟수:")
print(exit_page_summary)

print("\n평균 이탈률 및 평균 세션 지속 시간:")
print(summary_df)
```
