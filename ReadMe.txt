Application Name: ImageCropper
ImageCropper will help user to upload an image and get two cropped images having aspect ratio of 4:3 and 2:3.
Apart from that, user can also see details of program like Title, Description, Cast & Crews, Episode number etc. 
Finally, user will also be able to perform CRUD operation on the data using python script.

Setting up application:

Requirements:
Install nodeJS, XAMPP server, python, Angular 2(quickstart setup), code editor(visual studio code)

Steps:
1. get files for the project
   git clone https://github.com/gxg7435/ImageCropper 
2. cd Angular
3. open CMD in windows and do:
   npm install
   npm start
4. Application will fire up in browser. To use application:
   - click on upload image button and select image from this path ImageCropper/Angular/src/assets/images.
     It will display Movie name, description, and top three casts.
   - naviagte to the bottom and click on crop image button.
     It will show two crops (4:3 and 2:3 aspect ratio) in new page.
5. Open XAMPP server and start MYSQL server.
6. cd .. (Navigate out of Angular folder)
7. Execute python ImageCropper.py.
   It will add all the data(rootid,title,description,cast etc.) for the four rootid from the images into MySQL database.
   This would be our Worklist that multiple user can use.
