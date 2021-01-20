# WasteNot App 🍉
<img src="app/assets/Devpost Cover.png"/>

## Inspiration
According to the National Resources Defense Council, 40% of the food produced in America goes uneaten. This translates to about **$218 billion worth** of food that the nation wastes every year. One of the most significant reasons behind this is the misinterpretation of expiry or "best before" labels. Not only do these differ from country to country, but also from product to product. Thus, most consumers mistakenly believe date labels are safety indicators, which is why 90% report throwing away food once the expiration date arrives. Additionally, many consumers simply forget their fresh produce in their fridge or pantry.

This food waste is also taking a **big toll on our environment**. First, the resources spent creating food that gets thrown away include approximately: tens of millions of acres of cropland, 300 million barrels of oil, and 25% of freshwater usage in America alone. Second, this discarded food often winds up in landfills, where it contributes to harmful greenhouse gas emissions. Food waste makes up more than 20% of all content in American municipal landfills today.

**We need a universal, reliable, and accurate app that tracks these dates.**

## What it does
This is where WasteNot comes in. This mobile app reduces food waste by reminding the user about the items in their fridge before their projected expiry date.

## How we built it
After we brainstormed the idea, Jaclyn started bringing life to it by putting our thought out on Figma
Meanwhile, Disha and Kate found out what technology stack would be good. Since we needed to provide push notifications to the user, we came down to using React Native for creating Mobile Apps, and Python, Flask, and SQLAlchemy for our app's backend. The backend was deployed using Heroku and tested locally using Postman.
@Adriana created the app prototype using Jaclyn's design, generated mockups, converted the UI to into HTML/CSS code which would be the foundation for React Native UI and taking care of organizing our Github, DevPost and pitch.

## Challenges we ran into
It was hard to figure out what is the best tool to create our app idea given the small time in hand. We were juggling between a web app, a mobile app, drag and drop platforms like Thunkable, or platforms like Flutter React Native. We were all not very experienced using any of the frontend aspects of these tools, so we decided to try out React Native. Given the time constraints, we could only code the app partially.
Without a specialization in Microservices and React Native, our app still needs a lot of coding, but sooner than not, this simple yet thoughtful idea will come to life.
Another challenge was the timezone, so not all of us could work and sleep at the same time, although we tried to use it to our advantage as while some of us were sleeping, another was working!

## Accomplishments that we're proud of
We are absolutely happy about watching our idea come to life with everyone collaborating so well and smooth.
Kudos to @Jaclyn for managing this with her baby girl sitting on her lap!
We finished the app's initial backend! Our app currently has a database for scheduled grocery runs and food items. Users are able to create, add, update, and delete different food items as well as schedule, update, and delete grocery runs. Each request on the back-end returns a JSON response, and the live Heroku app for it can be found here, Now, we just need to work on absorbing it with the front-end!

## What we learned
Kate learned to apply her Python knowledge to application and learnt to deploy it to Heroku. @Disha started her journey on Mobile App Development at this hackathon and created our home screen @Jaclyn Learnt about a feature called overlays in Figma which helped her mimic buttons, animations, and cursors. @Adriana learned how to create user flows and a clickable, interactive prototype using Figma

## What's next for WasteNot
After completing the initial prototyped version using Figma, we wish to offer many more features such as:

An upload feature where the user can upload their grocery receipt and feed items, and add the product along with the details automatically.
A feature that provides the user with an estimate of the total money saved by the person by not letting an item expire
Using an API that can autofill the maximum days of freshness for particular common items rather than the user adding for each item. Our next challenge will be to code the app completely. We currently have a backend, partial frontend and the prototype, so our team will work on connecting the backend with a frontend aspect to complete the app.

