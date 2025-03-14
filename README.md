```
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from imagededup.methods import PHash
import os
import numpy as np

# Initialize Spark session
spark = SparkSession.builder.appName("ImageDeduplication").getOrCreate()

# Path to your image directory
image_dir = "/path/to/your/images"

# Read images as binary files
image_df = spark.read.format("binaryFile").load(image_dir)

# Initialize PHash object
phash = PHash()

# Define UDF to compute perceptual hash
def compute_phash(image_path):
    try:
        return phash.encode_image(image_path)
    except Exception as e:
        return None

# Register UDF with Spark
phash_udf = udf(compute_phash, StringType())

# Compute phash for each image
image_df = image_df.withColumn("phash", phash_udf(col("path")))

# Convert Spark DataFrame to Pandas for comparison
image_pd_df = image_df.select("path", "phash").toPandas()

# Define max distance threshold (adjust as needed)
max_distance_threshold = 10  # Adjust this value based on similarity criteria

# Function to calculate Hamming distance between two hashes
def hamming_distance(hash1, hash2):
    return np.sum(np.array(list(format(int(hash1, 16), '064b'))) != np.array(list(format(int(hash2, 16), '064b'))))

# Find similar images
similar_images = []
for i, (path1, hash1) in enumerate(image_pd_df.itertuples(index=False)):
    for j, (path2, hash2) in enumerate(image_pd_df.itertuples(index=False)):
        if i < j and hash1 and hash2:  # Avoid duplicate comparisons
            distance = hamming_distance(hash1, hash2)
            if distance <= max_distance_threshold:
                similar_images.append((path1, path2, distance))

# Save similar image results to a file
output_file = "/path/to/output/similar_images.txt"
with open(output_file, "w") as f:
    for img1, img2, dist in similar_images:
        f.write(f"Similar: {img1} <--> {img2} (Distance: {dist})\n")

print(f"Similar image list saved to: {output_file}")

```

```
import os
import shutil

# Define source and destination paths
source_dir = "/path/to/source_directory/subdirectory"  # Change to your subdirectory path
destination_dir = "/path/to/destination_directory"  # Change to your destination directory

# Ensure destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Copy all files from the source subdirectory to the destination directory
for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)
    destination_file = os.path.join(destination_dir, file_name)
    
    if os.path.isfile(source_file):  # Ensure it's a file
        shutil.copy2(source_file, destination_file)  # copy2 preserves metadata

print("Files copied successfully!")



```




# leetcode


```
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from imagededup.methods import PHash
import os

# Initialize Spark session
spark = SparkSession.builder.appName("ImageDeduplication").getOrCreate()

# Path to your image directory
image_dir = "/path/to/your/images"

# Read images as binary files
image_df = spark.read.format("binaryFile").load(image_dir)

# Initialize PHash object
phash = PHash()

# Define UDF to compute perceptual hash
def compute_phash(image_path):
    try:
        return phash.encode_image(image_path)
    except Exception as e:
        return None

# Register UDF with Spark
phash_udf = udf(compute_phash, StringType())

# Compute phash for each image
image_df = image_df.withColumn("phash", phash_udf(col("path")))

# Convert Spark DataFrame to Pandas to use imagededup for finding duplicates
image_pd_df = image_df.select("path", "phash").toPandas()

# Group by hash and find duplicates
duplicates = {}
for hash_value, group in image_pd_df.groupby("phash"):
    if len(group) > 1:
        duplicates[hash_value] = list(group["path"])

# Save duplicate results to a text file
output_file = "/path/to/output/duplicates.txt"
with open(output_file, "w") as f:
    for hash_value, paths in duplicates.items():
        f.write(f"Duplicate Group ({hash_value}):\n")
        f.write("\n".join(paths) + "\n\n")

print(f"Duplicate image list saved to: {output_file}")
```