from pyscript import document

name="Isabelle Rivera"
age=15
height=154.94
dream_vacay=["Bahamas, USA","Tokyo, Japan","London, UK"]
student_type=False
extra_abtme={"color":"red","car_brand":"Jeep","shoe_size":"6.5","best_friend":"my cat"}
fav_fruits=set(["bananas","grapes","apples","mangoes","cantaloupes"])
daysoftheweek=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")



output=f"""
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1"> <b> name </b> = {name} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(name).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> age </b> = {age} </p>
         <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(age).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> height </b> = {height} cm </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(height).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> dream_vacay </b> = {dream_vacay} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(dream_vacay).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> new student? </b> = {student_type} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(student_type).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> extra about me </b> = {extra_abtme} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(extra_abtme).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> fav fruits </b> = {fav_fruits} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(fav_fruits).__name__} </p>
        </div> 
        <div style="background-color: whitesmoke; width: 30%; padding: 1.5%; margin: 2%; box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px 3px; justify-self: center; border-radius: 15px;">
            <p style="line-height: 1;"> <b> days of the week </b> = {daysoftheweek} </p>
            <p style="text-align: right; line-height: 0.8;"> <b> data type: </b> {type(daysoftheweek).__name__} </p>
        </div> 
    </div>

"""

document.querySelector("#output").innerHTML = output