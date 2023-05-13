
from evennia import DefaultRoom, DefaultExit, utils, create_object
from ai.ai import ai_chat


class AIRoom(DefaultRoom):
    """
    A room that uses ai to generate a random description.

    """

    default_desc = "You see nothing special."
    prompt = ""

    def at_object_receive(self, moved_obj, source_location, move_type="move", **kwargs):
        if not utils.inherits_from(moved_obj, "evennia.objects.objects.DefaultCharacter"):
            return

        # check if room has already been ai generated
        if self.db.desc is not None and self.db.desc != "You see nothing special." and self.db.desc != self.default_desc:
            return

        moved_obj.msg(
            "You realize you are entering an area that has never been seen before...")

        print("Attempt AI generation of room description")

        # request room description from ai
        resp = ai_chat(self.prompt)
        resp = resp.strip()
        if resp == '':
            self.db.desc = self.default_desc
        else:
            self.db.desc = resp

        # TODO: this creates duplicate exits if an exit already exists. How to tell if an exit already exists? Maintain a grid maybe??
        # create additional exits
        new_room = ForestRoom
        if self.room_name == "Desert":
            new_room = DesertRoom
        elif self.room_name == "Mountain":
            new_room = MountainRoom
        elif self.room_name == "Swamp":
            new_room = SwampRoom

        exite = create_object(new_room, key=self.room_name)
        create_object(DefaultExit, key="east",
                      location=self, destination=exite)
        create_object(DefaultExit, key="west",
                      location=exite, destination=self)

        exitw = create_object(new_room, key=self.room_name)
        create_object(DefaultExit, key="west",
                      location=self, destination=exitw)
        create_object(DefaultExit, key="east",
                      location=exitw, destination=self)

        exits = create_object(new_room, key=self.room_name)
        create_object(DefaultExit, key="south",
                      location=self, destination=exits)
        create_object(DefaultExit, key="north",
                      location=exits, destination=self)

        exitn = create_object(new_room, key=self.room_name)
        create_object(DefaultExit, key="north",
                      location=self, destination=exitn)
        create_object(DefaultExit, key="south",
                      location=exitn, destination=self)


class ForestRoom(AIRoom):
    """
    A room that uses ai to generate a random description.

    """

    room_name = "Forest"
    default_desc = "You are in the midst of a lush and verdant forest."
    prompt = f"Provide a description of a deep forest area. It might have mushrooms or butterflies or animals grazing peacefully or something else not described."


class DesertRoom(AIRoom):
    """
    A room that uses ai to generate a random description.

    """

    room_name = "Desert"
    default_desc = "You are surrounded by an expansive desert."
    prompt = f"Provide a description of a sweltering desert area. It might have cacti or rocks or lizards scrambling around or something else not described."


class MountainRoom(AIRoom):
    """
    A room that uses ai to generate a random description.

    """

    room_name = "Mountain"
    default_desc = "You are on a chilly snow-covered mountain."
    prompt = f"Provide a description of a snowy mountainside area. It might have snow bluffs or trees covered in snow or something else not described."


class SwampRoom(AIRoom):
    """
    A room that uses ai to generate a random description.

    """

    room_name = "Swamp"
    default_desc = "You are in an old swamp."
    prompt = f"Provide a description of a decaying swamp area. It might have dying trees or frogs or smell terrible or something else not described."
