function Loginform(){
var email=document.getElementById('email').value;
if(email.indexOf('@')<=0){
    alert("invalid @ position");
    return false;
}
 if((email.charAt(email.length-4)!='.') && (email.charAt(email.length-3)!='.')){
    alert("invalid . position");
    return false;
}
var Password=document.getElementById('password');
if(Password.value.trim()==""){
    alert("Password should not be blank"); 
    return false;
}
 if(Password.value.length<5){
    alert("Password should be minimum 5 characters");
    return false;
}
 if(Password.value.length>12){
    alert("Password should be maximum 12 characters");
    return false;
}
}
function SignUpform(){
    var email=document.getElementById('Email').value;
if(email.indexOf('@')<=0){
    alert("invalid @ position");
    return false;
}
 if((email.charAt(email.length-4)!='.') && (email.charAt(email.length-3)!='.')){
    alert("invalid . position");
    return false;
}
var Password=document.getElementById("Password");
var CPassword=document.getElementById("cpassword");
 if(Password.value.trim()==""){
    alert("Password should not be blank"); 
    return false;
}
 if(Password.value.length<5){
    alert("Password should be minimum 5 characters");
    return false;
}
 if(Password.value.length>12){
    alert("Password should be maximum 12 characters");
    return false;
}
 if(Password.value!=CPassword.value){
    alert("Passwords are not matching");
    return false;
}
}