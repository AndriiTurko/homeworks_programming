import matplotlib.pyplot as plt
from PIL import Image

def build_graph(users, years, country):
    '''
    Builds a dependency chart of users and years in country
    '''
    plt.clf()
    users = [user/1000 for user in users]
    plt.plot(years, users, color='green', marker='o',
             linestyle='dashed', linewidth=2, markersize=10)
    plt.xlabel('YEARS')
    plt.ylabel('USERS(thousands)')

    plt.title('Internet users in ' + country)
    if len(years) <= 5:
        plt.xticks(years)
    plt.savefig('graphs/graph'+ country +'.jpg')
    resize_image('graphs/graph'+ country +'.jpg', 'graphs/graph'+ country +'.jpg', (400, 288))


 
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)

# build_graph([60917000, 7000000, 1517476, 1668422], [2000, 2001, 2002, 2003], 'Ukraine')