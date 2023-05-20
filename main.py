from web import create_app
from flask_apscheduler import APScheduler
from web.schedule_task import return_users


scheduler = APScheduler()


if __name__ == "__main__":
    scheduler.add_job(id='job1', func=return_users, trigger='interval', hours=4)
    scheduler.start()
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
    