# %% [markdown]
# # WK4 Descriptive Statistics <hr style= "border: 2.5px solid #126782"></hr>

# %% [markdown]
# Name: **Pia Mae D. Tolentino** <br>
# Course and Section: **BSCpE-2A**

# %% [markdown]
# Import **pandas**, **numpy**, and **matplotlib**.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# Create a **DataFrame** for "Jaguar-Panther-Data".

# %%
df = pd.read_csv("Jaguar-Panther-Data.csv")
df

# %% [markdown]
# Display a **concise summary** of the DataFrame.

# %%
df.info()

# %% [markdown]
# Display **summary statistics**.

# %%
df.describe()

# %% [markdown]
# ## Jaguar Analysis

# %% [markdown]
# Return the **mean** of Jaguar Performance.

# %%
jaguar_mean = df['Jaguar'].mean()
print ("Jaguar Performance Mean = " + str (jaguar_mean))

# %% [markdown]
# Display the *data type* of **jaguar_mean**.

# %%
type(jaguar_mean)

# %% [markdown]
# Return the **median** of Jaguar Performance.

# %%
jaguar_median = df['Jaguar'].median()
print ("Jaguar Performance Median = " + str (jaguar_median))

# %% [markdown]
# Display the *data type* of **jaguar_median**.

# %%
type(jaguar_median)

# %% [markdown]
# Return the **mode** of Jaguar Performance.

# %%
jaguar_mode = df['Jaguar'].mode()
print ("Jaguar Performance Mode = " + str (jaguar_mode))

# %% [markdown]
# Display the *data type* of **jaguar_mode**.

# %%
type(jaguar_mode)

# %% [markdown]
# Return the **range** of Jaguar Performance.

# %%
jaguar_range = df['Jaguar'].max() - df['Jaguar'].min()
print ("Jaguar Performance Range = " + str (jaguar_range))

# %% [markdown]
# Return the **variance** of Jaguar Performance.

# %%
jaguar_var = df['Jaguar'].var()
print ("Jaguar Performance Variance = " + str (jaguar_var))

# %% [markdown]
# Return the **standard deviation** of Jaguar Performance.

# %%
jaguar_sd = df['Jaguar'].std()
print ("Jaguar Performance Standard Deviation = " + str (jaguar_sd.round(1)))

# %% [markdown]
# Return the **coefficient of variation** for Jaguar Performance.

# %%
jaguar_cv = jaguar_sd/df['Jaguar'].mean()
print ("Jaguar Performance Coefficient of Variation = " + str (jaguar_cv.round(2)))

# %% [markdown]
# Visualize Jaguar Performance using **Boxplot**.

# %%
plt.boxplot(df['Jaguar'])
plt.title("Jaguar Performance Boxplot")
plt.xlabel("Jaguar")
plt.ylabel("Performance")
plt.xticks([])
plt.show()

# %% [markdown]
# ## Panther Analysis

# %% [markdown]
# Return the **mean** of Panther Performance.

# %%
panther_mean = df['Panther'].mean()
print ("Panther Performance Mean = " + str (panther_mean))

# %% [markdown]
# Display the *data type* of **panther_mean**.

# %%
type(panther_mean)

# %% [markdown]
# Return the **median** of Panther Performance.

# %%
panther_median = df['Panther'].median()
print ("Panther Performance Median = " + str (panther_median))

# %% [markdown]
# Display the *data type* of **panther_median**.

# %%
type(panther_median)

# %% [markdown]
# Return the **mode** of Panther Performance.

# %%
panther_mode = df['Panther'].mode()
print ("Panther Performance Mode = " + str (panther_mode))

# %% [markdown]
# Display the *data type* of **panther_mode**.

# %%
type(panther_mode)

# %% [markdown]
# Return the **range** of Panther Performance.

# %%
panther_range = df['Panther'].max() - df['Panther'].min()
print ("Panther Performance Range = " + str (panther_range))

# %% [markdown]
# Return the **variance** of Panther Performance.

# %%
panther_var = df['Panther'].var()
print ("Panther Performance Variance = " + str (panther_var))

# %% [markdown]
# Return the **standard deviation** of Panther Performance.

# %%
panther_sd = df['Panther'].std()
print ("Panther Performance Standard Deviation = " + str (panther_sd.round(1)))

# %% [markdown]
# Return the **coefficient of variation** for Panther Performance.

# %%
panther_cv = panther_sd/df['Panther'].mean()
print ("Panther Performance Coefficient of Variation = " + str (panther_cv.round(2)))

# %% [markdown]
# Visualize Panther Performance using **Boxplot**.

# %%
plt.boxplot(df['Panther'])
plt.title("Panther Performance Boxplot")
plt.xlabel("Panther")
plt.ylabel("Performance")
plt.xticks([])
plt.show()

# %% [markdown]
# ## **Hypothesis**

# %% [markdown]
# 


