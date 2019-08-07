import numpy as np
from sklearn.manifold import TSNE

def plot_embedding(data, label, title):
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    fig = plt.figure()
    #ax = plt.subplot(111)
    for i in range(data.shape[0]):
        plt.text(data[i, 0], data[i, 1], str(label[i]),
                 color=plt.cm.Set1((label[i] + 1) / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    return fig



def tnse():
    output, tSNE_features = model_T(features, adj_T)
    print("Generating T-SNE...")
    tsne = TSNE(n_components=2, init='pca', random_state=0)
    tSNE_result = tsne.fit_transform(tSNE_features.data.cpu().numpy())
    tSNE_label = labels.data.cpu().numpy()
    fig = plot_embedding(tSNE_result, tSNE_label,
                     't-SNE embedding of Cora'
                     )
    plt.show(fig)