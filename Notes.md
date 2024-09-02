### Model Training
When you train the model, run the model training script on the terminal as follows:
```
cd <app_root_folder>
cd home_prices_app
python3 -m scripts.train_model
```
Running it as a module adds all the constants on the path, making them accessible while training.

### Running Tests
On the terminal:
```
export PYTHONPATH=$(pwd)   
pytest
```
Through the debugger in VSCode:
1. Cmd + Shift + P to open the command pallete.
2. Python: Configure Tests
3. Select Pytest, and if prompted, select the test dir.
4. If this doesn't work, update the user settings.json to incluide the following
```
   {
        "python.testing.unittestEnabled": false,
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": [
            "tests"
        ]
   }
```