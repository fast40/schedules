# schedules
This project is a simple <a href="https://flask.palletsprojects.com/">flask</a> app that allows a group of friends to view each other's class schedules to see who is currently free to hang out. To configure the class schedules, create a `classes.json` file inside the `static` directory and list people and their classes with the following format (you should be able to paste this code as a simple example if you want):
```json
{
  "person_1": {
    "class_1": [
      {
        "start": "8:00am",
        "end": "10:30am",
        "days": [
          "monday",
          "wednesday"
        ]
      },
      {
        "start": "10:00am",
        "end": "12:00pm",
        "days": [
          "tuesday",
          "thursday"
        ]
      }
    ]
  }
}
```
You may find that copy/pasting following meeting format speeds up the somewhat manual process:
```json
{
  "start": "",
  "end": "",
  "days": [
    
  ]
}
```
After filling out the json file with many people, classes, and meeting times, you should see the website display something like the following:
<br>
<br>
<img src="https://github.com/fast40/schedules/blob/main/static/media/example-1.png?raw=true" alt="Example screenshot" width="300px">
