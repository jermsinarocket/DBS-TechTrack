<?php
session_start();

if (isset($_SESSION["token"])){
    header("Location: TechTrack-Page2.html");
}

$username = $_POST['username'];
$password = $_POST['password'];

$response = httpPost("http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login",
    array("username"=>$username,"password"=>$password));

$_SESSION["response"] = $response;

function httpPost($url, $data){
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    curl_close($curl);
    return $response;
}

?>