import requests
import json

# class Pokemon:
#     def __init__(self, id, nome, foto, tipo1, tipo2, golpes, abilities, evolve_to, foto2):
#         self.id = id
#         self.nome = nome
#         self.foto = foto
#         self.tipo1 = tipo1
#         self.tipo2 = tipo2
#         self.golpes = golpes
#         self.abilities = abilities
#         self.evolve = evolve_to #tentativa 2
#         self.foto2 = foto2



class Pokemon: # classe
    def __init__(self, nome):
        self.nome = nome.lower() # atributo

        self.id = 0           # atributo ;; tipo => int
        self.foto = ""        # atributo ;; tipo => string
        self.tipo1 = ""       # atributo ;; tipo => string
        self.tipo2 = ""       # atributo ;; tipo => string
        self.golpes = []      # atributo ;; tipo => list
        self.abilities = []   # atributo ;; tipo => list

        self.evolutions = [] # atributo ;; tipo => Pokemon

# pokemon a procurar
    def load_from_api(self):
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.nome}").text)

        self.id = res["id"] # 2
        self.foto = res["sprites"]["front_default"]

        for i in range(0, len(res["abilities"])):
            self.abilities.append(res["abilities"][i]["ability"]["name"])
        
        for i in range(0, len(res["moves"])):
            self.golpes.append(res["moves"][i]["move"]["name"])
        
        if len(res["types"]) == 2:
            self.tipo1 = res["types"][0]["type"]["name"]
            self.tipo2 = res["types"][1]["type"]["name"]
        else:
            self.tipo1 = res["types"][0]["type"]["name"]



    def evolve_chain(self):
        specie_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.nome}/").text)
        
        evolution_chain_url = specie_res['evolution_chain']['url']
        chain_search = json.loads(requests.get(evolution_chain_url).text)
        
        evo_chain = chain_search["chain"]
        
        list_sprite = []

        name = evo_chain["species"]["name"]
        poke_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text)
        sprite = poke_res["sprites"]["front_default"]
        list_sprite.append(sprite)
        print(list_sprite)


        for poke_evo in evo_chain["evolves_to"]:
            name = poke_evo["species"]["name"]
            poke_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text)
            sprite1 = poke_res["sprites"]["front_default"]
            list_sprite.append(sprite1)
            print(list_sprite)


            for poke_evo_evo in poke_evo["evolves_to"]:
                name = poke_evo_evo["species"]["name"]
                poke_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text)
                sprite2 = poke_res["sprites"]["front_default"]
                list_sprite.append(sprite2)
                print(list_sprite)

        self.evolutions = list_sprite


        # self.evolutions = sprite_form3


        #     evolutions = [sprite_1] + evolution_2
            # evolution_1.append(evolutions)
        
        # for evs in evolution_1:
        #     evolutions = [sprite] + evs
        #     self.evolutions.append(evolutions)

        # print(self.evolutions)
        #         evs => [ivysaur, venusaur]
            







    # def evolve_chain(self):
    #     specie_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.nome}/").text)
    #     evolution_chain_url = specie_res['evolution_chain']['url']
    #     chain_search = json.loads(requests.get(evolution_chain_url).text)
    #     evo_chain = chain_search["chain"]
    #     print(evo_chain["species"])

    #     for poke_evo in evo_chain["evolves_to"]:
    #         print(poke_evo["species"])
            
    #         for poke_evo_evo in poke_evo["evolves_to"]:
    #             print(poke_evo_evo["species"])
        
    #             # pokemonevo = Pokemon(self) 
    #             # pokemonevo.load_from_api()

    #             # self.evo1 = pokemonevo


# evolução do pokemon procurado
#     def evolve_from_api(self):
#         specie_res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.id}/").text)
#         evolution_chain_url = specie_res['evolution_chain']['url']
#         evolucao_res = json.loads(requests.get(evolution_chain_url).text)   #evolution-chain tentativa pessoal 2
        
#         if len(evolucao_res["chain"]["evolves_to"]):
#             nome = evolucao_res["chain"]["evolves_to"][0]["species"]["name"] # ivysaur
        

#             pokemon_evolution = Pokemon(nome) 
#             pokemon_evolution.load_from_api()

#             self.evolution = pokemon_evolution



# buscador dentro da evoluton-chain
# esse buscador vai procurar dentro da chain nomes especificos do pokemon q eu digitei previamente
# o buscador vai verificar a chain em que esse pokemon vive
# vai identificar o pokemon e a evolução, tudo dentro da chain

# var_chain = buscador de evolution-chain: https://pokeapi.co/api/v2/evolution-chain/{}, onde o dict é o id de familias evolutivas
# for pokeevo in range(len(var_chain)):
# procurando ["nome"] que correspondem de maneira igual ao pokemon procurado dentro das familias evolutivas







# <!-- <label>Evolves to</label>
#     <h3><p>{{pokemon.evo1.nome}}</p></h3>
#     <img src="{{pokemon.evo1.foto}}"><br>
#     <label>{{pokemon.evo1.tipo1}}</label>
#     <label>| {{pokemon.evo1.tipo2}}</label>
#     <hr> -->














# n da p fazer natures
# pq o api de natures é a lista geral de nature
# não os natures mais adequados para um pokemon





















# if __name__ == "__main__":
#     # pokemon = Pokemon("", "chimchar","","","","","","","")

#     piplup = Pokemon("piplup") # objeto
#     piplup.id = 1                           # atributo do objeto
#     piplup.tipo1 = "grass"                  # atributo do objeto
#     piplup.tipo2 = "poison"                 # atributo do objeto
#     piplup.foto = "<alguma foto legal>"     # atributo do objeto
#     piplup.golpes = []                      # atributo do objeto
#     piplup.abilities = []                   # atributo do objeto
#     piplup.print_info()
    
#     bulbasaur = Pokemon("bulbasaur") # objeto
#     bulbasaur.id = 1                           # atributo do objeto
#     bulbasaur.tipo1 = "grass"                  # atributo do objeto
#     bulbasaur.tipo2 = "poison"                 # atributo do objeto
#     bulbasaur.foto = "<alguma foto legal>"     # atributo do objeto
#     bulbasaur.golpes = []                      # atributo do objeto
#     bulbasaur.abilities = []                   # atributo do objeto

#     ivysaur = Pokemon("ivysaur")
#     ivysaur.id = 2                           # atributo do objeto
#     ivysaur.tipo1 = "grass"                  # atributo do objeto
#     ivysaur.tipo2 = "poison"                 # atributo do objeto
#     ivysaur.foto = "<alguma foto legal>"     # atributo do objeto
#     ivysaur.golpes = []                      # atributo do objeto
#     ivysaur.abilities = []                   # atributo do objeto

#     bulbasaur.evolve_to = ivysaur

#     venusaur = Pokemon("venusaur")
#     venusaur.id = 3                           # atributo do objeto
#     venusaur.tipo1 = "grass"                  # atributo do objeto
#     venusaur.tipo2 = "poison"                 # atributo do objeto
#     venusaur.foto = "<alguma foto legal>"     # atributo do objeto
#     venusaur.golpes = []                      # atributo do objeto
#     venusaur.abilities = []                   # atributo do objeto

#     ivysaur.evolve_to = venusaur
#     piplup.evolve_to = venusaur