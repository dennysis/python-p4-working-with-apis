import requests
import json


class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.text  # Use response.text instead of response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            if "agency" in program:
                programs_list.append(program["agency"])

        return programs_list


# Instantiate GetPrograms class
programs_instance = GetPrograms()

# Call program_school method
programs_schools = programs_instance.program_school()

# Print unique schools
for school in set(programs_schools):
    print(school)