from controllers.app_controller import createApp

from utils.create_db import create_db
from utils.config_db import config_db


if __name__ == "__main__":
    app = createApp()
    create_db(app)
    config_db(app)
    #app.run(debug=True)
    app.run()
