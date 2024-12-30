import tkinter

from google.googleData import GoogleData
from google.googleWebdrive import GoogleWebdrive
from google.modelGoogleSearch import ModelGoogleSearch


class App:
    def input_job_type(self) -> int:
        errorMsg = 'You did not enter a valid option.\n'
        while True:
            try:
                userJobType: int = int(input('Enter the number:\n1.Internship\n2.Job\n'))
            except ValueError:
                print(errorMsg)
                continue
            if 0 < userJobType < 3:
                break
            else:
                print(errorMsg)
                continue
        return userJobType

    def main_function(self, inputDict: dict, screenObj, root) -> None:

        url: str = ModelGoogleSearch(inputDict).url

        with GoogleWebdrive(url) as gwd:
            gwd.execute_on_enter()
            googleData = GoogleData(gwd.data, gwd.webElementList)

            googleData.display_msg_box(inputDict.__str__())
            googleData.log_data()
            googleData.generate_list_view(screenObj, root)


