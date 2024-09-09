import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.controller.chat_controller import router as chat_router
from src.controller.upload_controller import router as upload_router
from src.controller.delete_controller import router as delete_router
import uvicorn

# Set up logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

from src.environment.environment_utilities import load_environment_varibles, verify_environment_varibles

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(delete_router)

app.add_middleware(
    CORSMiddleware,
    # Adjust based on your frontend URL
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def startup_event():
    try:
        env_vars = load_environment_varibles()
        if env_vars is None:
            logging.error('Environment variables not loaded properly. load_environment_varibles() returned None.')
        else:
            count = 0
            for key, value in env_vars.items():
                # print(key, value)
                count += 1
                logging.info(f'Environment variables loaded: No. {count} : {key}')
        
        if not verify_environment_varibles(env_vars):
            logging.error('Environment variables verification failed.')
    except Exception as e:
        logging.error(f'An unexpected error occurred during startup: {e}')

@app.get('/api')
def hello():
    try:
        return {'hello': 'world'}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f"Error processing chat request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def main():
    print("Hello World")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=2)

if __name__ == "__main__":
    main()
