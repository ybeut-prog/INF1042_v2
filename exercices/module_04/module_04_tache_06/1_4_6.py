ensemble ={"rouge", "vert", "bleu"}
enleve ={"vert"}
n_fruit = {"jaune"}
#ensemble.discard("vert")
new_ensemble = ensemble-enleve
new = new_ensemble | n_fruit
print(new)