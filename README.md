# swapi-chall
## Description

Swapi Chall is a backend application built as proof of knowledge, it's a challenge.

## Installation
For install this application, you must build the code with Dockerfile to create a image, from this image, you are able to create a container that will serve this application
## Usage
This application consumes https://swapi.dev/ for gather information about the starwars spaceships, you can pass the 'mglt' parameter as a query string via Method Get to calculate how much stops each spaceship will take for specific mglt distance.
Ex:
https://swapi-chall-hxfe33oycq-ue.a.run.app/api?mglt=90000

For example: The Y-wing spaceship has:
- 1 week of consumables
- 80 MGLT per hour of performance

So if you want to know hoy much stops the Y-wing will take to run 10000 MGLT of distance, the application does:
1. Discover how much MGLT the Y-wing can run until the consumables getting over
    a. Change the 1 week of consumables into hours
    b. Multiply that hours by the MGLT per hour to find the autonomy of the spaceship
2. Calculate how much stops the Y-wing have to do.
    a. Divide the total distance by the autonomy in order to find how much stops the spaceship must to do for go thought all the distance

## Roadmap
1. Support POST comunications
2. Create a better UI interface

## Authors and acknowledgment
[@Naynivek](https://gitlab.com/naynivek)

