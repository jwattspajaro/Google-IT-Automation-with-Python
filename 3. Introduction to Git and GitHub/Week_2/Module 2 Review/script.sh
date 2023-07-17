# Explorar el repositorio
cat favorite_foods.log
./food_count.py
./food_question.py
git config user.name "Nombre"
git config user.email "usuario@ejemplo.com"

# Comprender el repositorio
git status
git log
git config user.name "Nombre"
git config user.email "usuario@ejemplo.com"

# Agregar una nueva función
git branch improve-output
git checkout improve-output
echo "print('Comida favorita, de más popular a menos popular')" >> food_count.py
./food_count.py
git add food_count.py
git commit -m "Agregando una línea en la salida que describe la utilidad del script food_count.py"

# Arreglar el script
./food_question.py
git log
git revert [ID-del-commit]
./food_question.py

# Operación de fusión
git checkout master
git merge improve-output
./food_question.py
git status
git log
