- python3 -m venv qr_env or 66_env
- ./ngrok http 8000 
- ngrok http 8000 (on Windows)
- .\qr_env\Scripts\activate.bat (On windows)
- source qr_env/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- uvicorn backend.main:app --reload
- VS Theme: 'Bluloco Dark theme', 'NoctisUva', 'Viow Flat', "Adapta Nikto"
- pip install fastapi-pagination[all]
- https://www.learmoreseekmore.com/2021/02/vue3-vue-tailwind-pagination.html
    npm install --save @ocrv/vue-tailwind-pagination
- 


fastapi==0.66.1
uvicorn
sqlalchemy
passlib[bcrypt]
python-jose
python-multipart
fastapi-pagination[all]==0.8.3
