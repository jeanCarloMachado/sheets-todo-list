import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


class Sheet:
    @staticmethod
    def initailize():
        scope = ['https://spreadsheets.google.com/feeds']
        this_file_dir = os.path.dirname(os.path.realpath(__file__))
        credentials = ServiceAccountCredentials.from_json_keyfile_name(f'{this_file_dir}/../credentials.json', scope)
        gc = gspread.authorize(credentials)

        sh = gc.open_by_key('16IEVEWcVN36Fxw-mjgW_1FEW7GeGytm8O8_y9iFEiNc')
        worksheet = sh.get_worksheet(0)

        return worksheet