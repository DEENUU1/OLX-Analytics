from flask_apscheduler import APScheduler

from base.schedule.schedule_task import (
    schedule_report,
    send_newest_offers,
    send_weekly_reports_to_users,
)
from web import create_app

scheduler = APScheduler()


if __name__ == "__main__":
    scheduler.add_job(id="job1", func=send_newest_offers, trigger="interval", hours=4)
    scheduler.add_job(id="job2", func=schedule_report, trigger="interval", days=1)
    scheduler.add_job(
        id="job3", func=send_weekly_reports_to_users, trigger="interval", days=7
    )
    scheduler.start()
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
