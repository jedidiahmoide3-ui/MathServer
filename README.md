# Ex.04 Design a Website for Server Side Processing
## Date:15-03-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
    <head>
        <title></title>
    </head>
    <style>
          body
          {
            background:linear-gradient(45deg,rgb(185, 45, 45),rgb(190, 12, 210));
            margin:10px;
          }  
          .head
          {
            gap:40px;
            position: fixed;
            bottom:10%;
            left:35%;
            border: dashed 4px rgb(255, 255, 255);
            border-radius: 20px;
            background: rgb(255, 209, 23);
            padding:100px;
          }
          input
         {
            margin-top: 10px;
            padding: 8px;
            border-radius: 20px;
         }
         .form
         {
            border-radius: 10px;
            width:10px;
         }
         .submit
         {
            color:black;
            background-color: rgba(255, 255, 255, 0.642);
         }
          
    </style>
    <body>
        <center>
            <div class="head">
                <h1>PRICE CALCULATER</h1>
                <h2>JEDIDIAH M D (25012775)</h2>
                <form method="POST">
                    {% csrf_token %}
                <label>PRICE:</label>
                <input type="text" name="PRICE" value="{{Price}}">
                <br><br>
                <label>GST:</label>
                <input type="text" name="GST" value="{{GST}}">
                <br><br>
                <input type="submit" value="CALCULATE">
                <br><br>
                <label>TOTAL:</label>
                <input type="text" value="{{Total}}">
                </form>
            </div>
        </center>
    </body>
</html>

views.py 

from django.shortcuts import render
def Calculate_bill(request):
    price = float(request.POST.get('PRICE','0'))
    gst = float(request.POST.get('GST','0'))
    total = price + (price * gst / 100) if request.method == 'POST' else 0
    print("Price =", price)
    print("GST =", gst)
    print("Total =", total)
    return render(request,"mathapp/math.html",
    {'Price':price,'GST':gst,'Total':total})

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.Calculate_bill, name='Calculate_bill')
    ]

```

## OUTPUT - SERVER SIDE:

![alt text](<Screenshot 2026-03-16 000500.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-03-16 000530.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
