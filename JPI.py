
import webbrowser
STUDENT=['ABDULLAH','MAHIBUL','PARTHO','JUBAER','AKASH','CHAYON','ABUJAR','SALMAN','ABIR','NAFISA','RABBY','KHOKON','SOWROV','ARAFAT','SAGOR','RAYHAN','ABIR','LIMON','ASIF','SHUVRO','SABBAB','ANIK','RABEYA','MEHADI','TAMIM','SHAKIL','SHAFIQUL','ROTHEN','ZAYED','RIYED','NAHID','ASHIF','MUSTAKIN','AFRIDI','SAZID','FAYSAL','FAHIM','JEHAD','URFE','SIMI','MAHIA','RANI','RUMPA','ADRITA','HANA','ROHAN']
for i in range(1,3):
    name1 =input("Enter your name :")
    name =name1.upper()
    if name =="NAHID":
        admin= input("ENTER YOUR PASSWORD  TO ACCESS ADMIN PANNEL :")
        if admin =="119887":
            print("NAHID INFO")
    if name in STUDENT:
        print(f"YES {name} IS A STUDENT OF JASHORE POLYTECHNIC INSTITUTE !")
    else:
        print(f" NO {name} IS NOT A STUDENT OF THIS COLLAGE")
print("Cradit Limit Is Over.")
site =input("Earn cradit to press 1 and enter :")
if site =="1":
    webbrowser.open_new("https://sites.google.com/view/nahidul407/home")
print("LOVE YOU JAN . ONK VALO BASE AJ O TOKA . JAIDIN TAKA HOBA TOR SAMNA DIYA TAKA URAITA URAITA JABO.")
