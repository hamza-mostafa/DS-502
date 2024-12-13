## Step 2: Install Dependencies Using `pip`

You can use the `requirements.txt` file to install the dependencies in any environment.

### Using a Virtual Environment
1. **Activate your virtual environment:**
   - For **venv**:
     ```bash
     source venv/bin/activate    # On Linux/Mac
     venv\Scripts\activate       # On Windows
     ```

   - For **Conda**:
     ```bash
     conda activate <your-env-name>
     ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
### Using Jupyter Notebooks

If you’re using a Jupyter Notebook, you can install the dependencies directly within a cell:
   ```jupyter
   !pip install -r requirements.txt
   ```
   
