nom="Pain"
prix_unitaire=2
quantite_en_stock= 15

print(f"L'article {nom} coute {prix_unitaire} euros, il en reste {quantite_en_stock} en stock.")


ajout_de_stock=int(input("Combien de stock en ajout ?"))
quantite_en_stock+=ajout_de_stock
print

print("Stock aprés ajout:" , quantite_en_stock)


quantite_demander=int(input("Combien de quantité desirez vous ?"))
quantite_en_stock-=quantite_demander
print("Stock restant:", quantite_en_stock)

augmentation_prix= 0.10
prix_unitaire*= (1+ augmentation_prix)
print("Prix unitaire:" , prix_unitaire)

print(f"L'article {nom} coute {prix_unitaire} euros, il en reste {quantite_en_stock} en stock.")







