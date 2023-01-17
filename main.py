from fastapi import FastAPI, Request, Response, HTTPException
from pandas import DataFrame
from datetime import date, timedelta, datetime

app = FastAPI()
period_length = timedelta(minutes=30)


def generate_calendar(start_date: date, end_date: date):
    """Return half-hourly periods between start_date (inclusive) and end_date (exclusive)"""
    start_dt = datetime(year=start_date.year,
                        month=start_date.month,
                        day=start_date.day)

    # two periods per hour in a day
    period_count = (end_date - start_date).days * 24 * 2
    periods = [(
        (start_dt + period_length * i).date(), #.isoformat(),
        (start_dt + period_length * i).time(), #.isoformat()[0:5],
        i % 48 + 1
    ) for i in range(period_count)]

    return DataFrame.from_records(periods, columns=["Date", "Time", "Period"])


@app.get("/calendar")
def get_calendar(request: Request):
    try:
        start_date = date.fromisoformat(request.query_params.get("start_date"))
        end_date = date.fromisoformat(request.query_params.get("end_date"))
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Both 'start_date' and 'end_date' must be provided as query parameters in the ISO date format, e.g. '2023-01-01'")

    return Response(generate_calendar(start_date, end_date).to_json(orient="records", date_format="iso"), media_type="application/json")
