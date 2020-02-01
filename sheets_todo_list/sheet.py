import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    @staticmethod
    def initailize():
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('./credentials.json', scope)
        gc = gspread.authorize(credentials)

        sh = gc.open_by_key('16IEVEWcVN36Fxw-mjgW_1FEW7GeGytm8O8_y9iFEiNc')
        worksheet = sh.get_worksheet(0)

        return worksheet