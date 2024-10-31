import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def load_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        # Skip the header line if present
        next(file, None)  # This skips the first line
        for line in file:
            x, y = map(float, line.strip().split(','))
            points.append(Point(x, y))
    return points


def plot_points(points, color, label):
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]
    plt.scatter(x_coords, y_coords, color=color, label=label)


def scatter_plot():
    filename = 'C:/Users/MY PC/Downloads/x_y_coordinates.txt'
    points = load_points_from_file(filename)

    # Initial plot
    plot_points(points, 'blue', 'Original Points')

    # Translate points
    dx, dy = 2, 3  # Translation values
    for point in points:
        point.translate(dx, dy)

    # Replot translated points
    plot_points(points, 'red', 'Translated Points')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Point Translation')
    plt.grid()
    plt.legend()
    plt.show()



if __name__ == '__main__':
    scatter_plot()