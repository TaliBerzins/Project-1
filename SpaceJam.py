from direct.showbase.ShowBase import ShowBase
import math, sys, random
from panda3d.core import Vec3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        self.fighter = self.loader.loadModel('./Assets/Player/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0,0.0,0.0,1.0)
        self.fighter.setScale(200)
        self.fighter.setPos(500,500,500)



        self.accept('escape', self.quit)

        # Camera movement
        self.moveSpeed = 500
        self.mouseSensitivity = 100

        # Camera rotation
        self.cameraHeading = 0
        self.cameraPitch = 0

        # Movement keys
        self.keys = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        # W/S/A/D
        self.accept("w", self.setKey, ["forward", True])
        self.accept("w-up", self.setKey, ["forward", False])

        self.accept("s", self.setKey, ["backward", True])
        self.accept("s-up", self.setKey, ["backward", False])

        self.accept("a", self.setKey, ["left", True])
        self.accept("a-up", self.setKey, ["left", False])

        self.accept("d", self.setKey, ["right", True])
        self.accept("d-up", self.setKey, ["right", False])

        # Space / Shift
        self.accept("space", self.setKey, ["up", True])
        self.accept("space-up", self.setKey, ["up", False])

        self.accept("shift", self.setKey, ["down", True])
        self.accept("shift-up", self.setKey, ["down", False])

        # Mouse
        self.accept("mouse1", self.startMouseLook)
        self.accept("mouse1-up", self.stopMouseLook)

        self.mouseLooking = False

        # Mouse wheel
        self.accept("wheel_up", self.moveForward)
        self.accept("wheel_down", self.moveBackward)

        # Update every frame
        self.taskMgr.add(self.updateCamera, "updateCamera")


        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        texture = self.loader.loadTexture("./Assets/Universe/images.jpeg")
        self.Universe.setTexture(texture,1)

        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setScale(150)
        texture = self.loader.loadTexture("./Assets/Space Station/SpaceStation1_Dif2.png")
        self.SpaceStation.setTexture(texture,1)
        self.SpaceStation.setPos(1000, 1500, 100)



        self.planets = []
        

        # Load planets
        for i in range(1, 7):


            texturePath = f"./Assets/Planets/images-{i}.jpeg"

            # Load texture
            texture = self.loader.loadTexture(texturePath)

            if texture is None:
                print(f"COULD NOT LOAD PLANET {i} TEXTURE!")
                continue

            print(f"Planet {i} texture loaded!")

            # Load sphere
            planet =  self.loader.loadModel("./Assets/Planets/protoPlanet.x")


            # Put planet into the scene
            planet.reparentTo(self.render)

            # Apply texture
            planet.setTexture(texture, 1)

            # Turn off lighting
            planet.setLightOff()
            planet.setShaderOff()

            # Position planet
            planet.setPos(150, 2500 + (i - 1) * 500, 67)

            # Size planet
            planet.setScale(150)

            self.planets.append(planet)









    def setKey(self, key, value):
        self.keys[key] = value


    def startMouseLook(self):
        self.mouseLooking = True


    def stopMouseLook(self):
        self.mouseLooking = False


    def moveForward(self):
        self.camera.setY(self.camera.getY() + 200)


    def moveBackward(self):
        self.camera.setY(self.camera.getY() - 200)


    def updateCamera(self, task):

        dt = globalClock.getDt()

        # -------------------------
        # Mouse rotation
        # -------------------------

        if self.mouseLooking and self.mouseWatcherNode.hasMouse():

            mouseX = self.mouseWatcherNode.getMouseX()
            mouseY = self.mouseWatcherNode.getMouseY()

            self.cameraHeading -= mouseX * self.mouseSensitivity * dt
            self.cameraPitch += mouseY * self.mouseSensitivity * dt

            # Prevent camera from flipping upside down
            self.cameraPitch = max(-89, min(89, self.cameraPitch))

            self.camera.setHpr(
                self.cameraHeading,
                self.cameraPitch,
                0
            )

        # -------------------------
        # Keyboard movement
        # -------------------------

        movement = Vec3(0, 0, 0)

        if self.keys["forward"]:
            movement.y += 1

        if self.keys["backward"]:
            movement.y -= 1

        if self.keys["left"]:
            movement.x -= 1

        if self.keys["right"]:
            movement.x += 1

        if self.keys["up"]:
            movement.z += 1

        if self.keys["down"]:
            movement.z -= 1

        # Normalize so diagonal movement isn't faster
        if movement.length() > 0:
            movement.normalize()

            movement *= self.moveSpeed * dt

            # Move relative to camera's orientation
            self.camera.setPos(
                self.camera,
                movement
            )

        return task.cont

    def quit(self):
        sys.exit()
    
    


app = MyApp()
app.run()

#Link for planet picture https://www.nbcnews.com/mach/science/what-dwarf-planet-ncna926751
#Link for planet picture - image 6 - https://www.nhm.ac.uk/discover/planet-mercury.html
#Link for planet picture - image 2 - https://esawebb.org/wordbank/planet/
#Link for planet picture - image 3 - https://www.sciencedaily.com/releases/2026/01/260101160859.htm
#Link for planet picture - image 4 - https://www.space.com/25986-planet-definition.html
#Link for planet picture - image 5 - https://www.wired.com/story/scientists-scan-mysterious-planet-as-it-drifts-through-space/
#Universe picture https://www.newscientist.com/article/2524208-100-year-old-assumption-about-the-universe-may-soon-be-overturned/
#Space ship - https://www.artstation.com/artwork/YqvZq