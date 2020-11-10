# EduTools
Winner of HackPHS 2020
## Inspiration
As the COVID19 pandemic worsens globally, online learning has severely impacted inequality as schools are forced to decide between putting lives at risk and providing an accessible education. 

Phone ownership is vastly more widespread than consistent internet access. Just 6% of children in eastern and southern Africa have access to the internet, yet cell phone ownership can be as high as 82%.

## What it does:
EduTools makes traditional online learning accessible without the need of internet access, all you need is a basic phone. 

## How I built it:
- Twilio API to receive/send SMS messages
- Flask backend to process and organize communication
- State of the art natural language processing APIs for Wikipedia, translation, and grammar checking, OCR & Wolfram|Alpha for math solving

## Challenges:
- Many APIs are out of date, so we had to modify and customize many queries to ensure proper functionality and error handling
- Integration of OCR and Wolfram|Alpha was difficult, and we needed to tune settings to optimize both image recognition and equation solving, and fitting everything into a text message
- Styling the teacher portal was difficult, and designing for both practicality and aesthetics meant we needed to compromise in many aspects

## Accomplishments that we're proud of:
- Developing a consistent, user-friendly cross-platform API for mobile SMS usage
- Optimizing the number of text messages (many SMS plans are limited, so we want to be efficient in communication)
- Developing and iterating on an early prototype, adding diversity of functionality, from english and math to foreign language and general knowledge

## What I learned:
- Starting off with organized planning documents is super important: all the object oriented programming design was scripted out in UML diagrams, and the UI mockups were designed in Adobe Illustrator
- Having testers quickly highlights bugs and unanticipated actions, continuous testing and refactoring quickly increased user experience

## What's next:
- More features! School isn't just academics; we can include functionality for clubs, sports, community service, and other events
- Additional student resources: recipe finders, meditation, and workouts

## Built With
Love

## Contributors
David, Daniel, Rohit, Nate 