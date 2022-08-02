import config
from sqlalchemy import create_engine
import getNewTaskData
import updateJiraData


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            config.user, config.password, config.host, config.port, config.database
        )
    )

if __name__ == '__main__':
    try:
        engine = get_connection()
        print( f"Connection to {config.host} for user {config.user} created successfully")

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

    else:
        # Do the logic
        connection = engine.connect()
