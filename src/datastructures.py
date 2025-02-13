
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member["last_name"] = self.last_name
        member.setdefault("id", self._generateId()) # Si no pongo el setDefault del ID la funcion _generateId sobreescribe al ID 3443 que el test quiere asignar
        member["lucky_numbers"] = member.get("lucky_numbers") # Busca la clave "lucky_numbers" en el diccionario member 
        return member
        

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id: # Busca un miembro segun la posicion del indice del bucle con un id especifico en la lista self._members
                del self._members[position]
                return {"done": True}
        return {"done": False}


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return {
                "first_name": member["first_name"],
                "id": member["id"],
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
                }
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
