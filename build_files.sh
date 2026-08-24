echo "Building the project..."
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "Make Migration..."
python3.12 manage.py make-migrations --noinput
python3.12 manage.py migrate --noinput
echo "BUILD END"