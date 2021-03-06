1.机器学习概念
	(1) 有监督学习：监督学习是学习给定标签的数据集，比如说有一组病人，给出他们的详细资料，将他们是否已确诊癌症作为标签，然后预测一名（其他的）病人是否会患有癌症，就是一种典型的监督学习。监督学习中也有不同的分类，如果我们训练的结果是得癌症和不得癌症之类离散的类型，则称为分类（Classification），如果只有两种类型的话可以进一步称为二分类（Binary Classification）；如果我们训练的结果是得癌症的概率为0.87之类连续的数字，则称为回归（Regression）
		回归问题往往会通过计算误差（Error）来确定模型的精确性。误差由于训练集和验证集的不同，会被分为训练误差（Training Error）和验证误差（Validation Error）。但值得注意的是，模型并不是误差越小就一定越好，因为如果仅仅基于误差，我们可能会得到一个过拟合（Overfitting）的模型；但是如果不考虑误差，我们可能会得到一个欠拟合（Underfitting）的模型
		分类问题衡量结果精度的有一些相关术语，首当其冲的是准确率（Accuracy）、精确率（Precision）和召回率（Recall）。这三个词汇应用于二分类问题：将数据分为正例（Positive Class）和反例（Negative Class），准确率是预测和标签一致的样本在所有样本中所占的比例；精确率是你预测为正类的数据中，有多少确实是正类；召回率是所有正类的数据中，你预测为正类的数据有多少。这三个数据往往用来衡量一个二分类算法的优劣
	(2) 无监督学习：无监督学习是学习没有标签的数据集，比如在分析大量语句之后，训练出一个模型将较为接近的词分为一类，而后可以根据一个新的词在句子中的用法（和其他信息）将这个词分入某一类中。其中比较微妙的地方在于，这种问题下使用聚类（Clustering）（方法）所获得的簇（Cluster）（结果），有时候是无法人为地观察出其特征的，但是在得到聚类后，可能会对数据集有新的启发
		聚类问题的标准一般基于距离：簇内距离（Intra-cluster Distance）和簇间距离（Inter-cluster Distance）。根据常识而言，簇内距离是越小越好，也就是簇内的元素越相似越好；而簇间距离越大越好，也就是说簇间（不同簇）元素越不相同越好。一般来说，衡量聚类问题会给出一个结合簇内距离和簇间距离的公式。
	(3) 泛化能力：训练模型会把数据分成三部分 训练集，交叉验证集，测试集 ；模型中对新数据的预测能力。在实际中如果对训练数据能很好的拟合，而对验证集的效果较差，泛化能力较弱，可能出现过拟合。
	(4)过拟合和欠拟合：
		1.过拟合：就是训练时的结果很好，但是在预测时结果不好的情况。
		2.产生过拟合的原因：
		（1) 模型的复杂度太高。比如：网络太深，
		（2）过多的变量（特征）
		（3）训练数据非常少。
		3.如何解决过拟合？
		（1）尽量减少选取变量的数量。
			可以人工检查每一项变量，并确定哪些变量更重要。然后保留那些更重要的特征变量。
			可以使用模型选择算法，通过该算法自动的选择使用哪些特征变量，舍弃哪些特征变量。
		（2）正则化
			正则化会保留所有的特征变量，但是会减小特征变量的数量级。
			这种方法非常有效，当我们有很多特征变量时，其中每一个特征变量都对预测产生了一些影响。每一个变量都有用，因此我们希望保留所有的变量，这个时候就可以使用正则化的方法。
			正则化就是使用惩罚项，通过惩罚项，我们可以将一些参数的值变小。通常参数值越小，对应的函数也就越光滑，也就是更加简单的函数，因此不容易发生过拟合问题。
		（3）数据集扩增（Data augmentation）
			“有时候不是因为算法好赢了，而是因为拥有更多的数据才赢了。”
			不记得原话是哪位大牛说的了，hinton？从中可见训练数据有多么重要，特别是在深度学习方法中，更多的训练数据，意味着可以用更深的网络，训练出更好的模型。
			既然这样，收集更多的数据不就行啦？如果能够收集更多可以用的数据，当然好。但是很多时候，收集更多的数据意味着需要耗费更多的人力物力，有弄过人工标注的同学就知道，效率特别低，简直是粗活。
			所以，可以在原始数据上做些改动，得到更多的数据，以图片数据集举例，可以做各种变换，如：
				将原始图片旋转一个小角度
				添加随机噪声
				一些有弹性的畸变（elastic distortions），论文《Best practices for convolutional neural networks applied to visual document analysis》对MNIST做了各种变种扩增。
				截取（crop）原始图片的一部分。比如DeepID中，从一副人脸图中，截取出了100个小patch作为训练数据，极大地增加了数据集。感兴趣的可以看《Deep learning face representation from predicting 10,000 classes》.
		（4)dropout
			Dropout则是通过修改神经网络本身来实现的，它是在训练网络时用的一种技巧（trike）
		（5）重新清洗数据。
			导致过拟合的一个原因也有可能是数据不纯导致的，如果出现了过拟合就需要我们重新清洗数据
		
		1.什么是欠拟合？模型没有很好地捕捉到数据特征，不能够很好地拟合数据的情况，就是欠拟合。
		2.为什么会产生欠拟合？因为模型不够复杂而无法捕捉数据基本关系，导致模型错误的表示数据。
		3.怎么解决欠拟合？
		（1）添加其他特征项，有时候我们模型出现欠拟合的时候是因为特征项不够导致的，可以添加其他特征项来很好地解决。例如，“组合”、“泛化”、“相关性”三类特征是特征添加的重要手段，无论在什么场景，都可以照葫芦画瓢，总会得到意想不到的效果。除上面的特征之外，“上下文特征”、“平台特征”等等，都可以作为特征添加的首选项。
		（2）添加多项式特征，这个在机器学习算法里面用的很普遍，例如将线性模型通过添加二次项或者三次项使模型泛化能力更强。例如上面的图片的例子。
		（3）减少正则化参数，正则化的目的是用来防止过拟合的，但是现在模型出现了欠拟合，则需要减少正则化参数。
		什么是Bias(偏差)：Bias反映的是模型在样本上的输出与真实值之间的误差，即模型本身的精准度，即算法本身的拟合能力
		什么是Variance(方差)：Variance反映的是模型每一次输出结果与模型输出期望之间的误差，即模型的稳定性。反应预测的波动情况。
		什么是Noise(噪声)：这就简单了，就不是你想要的真正数据，你可以想象为来破坏你实验的元凶和造成你可能过拟合的原因之一，至于为什么是过拟合的原因，因为模型过度追求Low Bias会导致训练过度，对测试集判断表现优秀，导致噪声点也被拟合进去了
	（5）交叉验证：判断模型的好和坏，就是衡量模型的（方差+偏差）和的最小值。因此主要的关注点就是平衡Bias和Variance。现在通用的衡量方法采用的是交叉验证的思想。交叉验证思想能够很好的处理方差大和偏差大这两大痛点，能够更好的评估模型好坏！	
		叉验证的目的：在实际训练中，模型通常对训练数据好，但是对训练数据之外的数据拟合程度差。用于评价模型的泛化能力，从而进行模型选择。
		交叉验证的基本思想：把在某种意义下将原始数据(dataset)进行分组,一部分做为训练集(train set),另一部分做为验证集(validation set or test set),首先用训练集对模型进行训练,再利用验证集来测试模型的泛化误差。另外，现实中数据总是有限的，为了对数据形成重用，从而提出k-折叠交叉验证。
		对于个分类或回归问题，假设可选的模型为。k-折叠交叉验证就是将训练集的1/k作为测试集，每个模型训练k次，测试k次，错误率为k次的平均，最终选择平均率最小的模型Mi。
		
2.线性回归原理：
	线性回归是利用数理统计中回归分析，来确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法，运用十分广泛。其表达形式为y = w'x+e，e为误差服从均值为0的正态分布。 [1] 
		回归分析中，只包括一个自变量和一个因变量，且二者的关系可用一条直线近似表示，这种回归分析称为一元线性回归分析。如果回归分析中包括两个或两个以上的自变量，且因变量和自变量之间是线性关系，则称为多元线性回归分析。
		
3.线性回归的损失函数，代价函数，目标函数 
		假设训练集数量是m ,X = [x0,x1,x2...x(m-1)] , b 代表参数,θ代表变量 = [w0,w1,w2...w(m-1)]  α 代表学习率
		目标函数 ：h(X) = np.dot(θ.T,X) +b
		损失函数：J（θ）= 1/2m * (h(X)-y).T * (h(X)-y)
		代价函数：θ ：= θ - α*np.dot((h(X)-y),X)/m
		
4.优化方法： （梯度下降法，牛顿法，拟牛顿法）
	(1)梯度下降法：
		1）首先对θ赋值，这个值可以是随机的，也可以是一个零向量；
		2）改变θ的值，使得J(θ)按梯度下降的方向进行减少；
		3）当J(θ)下降到无法下降时为止，即J(θ)对θ的导数为0时，比较J(θ)的值是否有变化。
	(2)牛顿法：
		无约束条件的最优化问题，假设目标函数J(θ)J(θ)具有二阶连续偏导数，若第kk次迭代值为 θ(k)θ(k)，则可将J(θ(k+1))J(θ(k+1))在θ(k)θ(k)附近进行二阶泰勒展开：
		J(θ(k+1))=J(θ(k))+J′(θ(k))(θ(k+1)−θ(k))+12J′′(θ(k))(θ(k+1)−θ(k))2
		J(θ(k+1))=J(θ(k))+J′(θ(k))(θ(k+1)−θ(k))+12J″(θ(k))(θ(k+1)−θ(k))2
		如果 θ(k+1)θ(k+1)趋近于θ(k)θ(k)时，limθ(k+1)−θ(k)→0J(θ(k+1))−J(θ(k))=0limθ(k+1)−θ(k)→0J(θ(k+1))−J(θ(k))=0，带入上式，可以得到更新参数集合θθ的迭代公式：
		θ(k+1)=θ(k)−J′(θ(k))J′′(θ(k))
		θ(k+1)=θ(k)−J′(θ(k))J″(θ(k))
		其中，J′′(θ(k))J″(θ(k))为J(θ(k))J(θ(k))的海塞矩阵（Hesse Matrix），上式中[J′′(θ(k))]−1[J″(θ(k))]−1即为海塞矩阵的逆矩阵。


	(3)拟牛顿法：
		由于牛顿法中海塞矩阵的逆矩阵计算相对复杂，拟牛顿法通过一个nn阶矩阵G(θ(k))G(θ(k))来近似代替[J′′(θ(k))]−1[J″(θ(k))]−1。 
		牛顿法中，海塞矩阵需要满足条件：
		J′(θ(k+1))−J′(θ(k))=J′′(θ(k))(θ(k+1)−θ(k))
		J′(θ(k+1))−J′(θ(k))=J″(θ(k))(θ(k+1)−θ(k))
		上式变形，得到拟牛顿条件：
		[J′′(θ(k))]−1(J′(θ(k+1))−J′(θ(k)))=θ(k+1)−θ(k)
		[J″(θ(k))]−1(J′(θ(k+1))−J′(θ(k)))=θ(k+1)−θ(k)
		拟牛顿法将G(θ(k))G(θ(k))作为[J′′(θ(k))]−1[J″(θ(k))]−1的近似，则G(θ(k))G(θ(k))需要满足如下条件： 
		1）每次迭代矩阵G(θ(k))G(θ(k))为正定矩阵； 
		2）G(θ(k))G(θ(k))满足拟牛顿条件，即 G(θ(k))(J′(θ(k+1))−J′(θ(k)))=θ(k+1)−θ(k)G(θ(k))(J′(θ(k+1))−J′(θ(k)))=θ(k+1)−θ(k)。 
		
		
5.线性回归的评估指标
	(1)、残差估计
		总体思想是计算实际值与预测值间的差值简称残差。从而实现对回归模型的评估，一般可以画出残差图，进行分析评估、估计模型的异常值、同时还可以检查模型是否是线性的、以及误差是否随机分布
	(2)、均方误差(Mean Squared Error, MSE)
		均方误差是线性模型拟合过程中，最小化误差平方和(SSE)代价函数的平均值。MSE可以用于不同模型的比较，或是通过网格搜索进行参数调优，以及交叉验证等。
	(3)、决定系数
		可以看做是MSE的标准化版本，用于更好地解释模型的性能。换句话说，决定系数是模型捕获相应反差的分数。


6.sklearn参数详解
		1.获取数据
			1.1 导入sklearn数据集
	　　		sklearn中包含了大量的优质的数据集，在你学习机器学习的过程中，你可以通过使用这些数据集实现出不同的模型，从而提高你的动手实践能力，同时这个过程也可以加深你对理论知识的理解和把握。（这一步我也亟需加强，一起加油！^-^）
				首先呢，要想使用sklearn中的数据集，必须导入datasets模块：
					from sklearn import datasets
					iris = datasets.load_iris() # 导入数据集
					X = iris.data # 获得其特征向量
					y = iris.target # 获得样本label
			1.2 创建数据集
				你除了可以使用sklearn自带的数据集，还可以自己去创建训练样本
					from sklearn.datasets.samples_generator import make_classification
					X, y = make_classification(n_samples=6, n_features=5, n_informative=2, 
						n_redundant=2, n_classes=2, n_clusters_per_class=2, scale=1.0, 
						random_state=20)
					# n_samples：指定样本数
					# n_features：指定特征数
					# n_classes：指定几分类
					# random_state：随机种子，使得随机状可重
		2. 数据预处理
　　		数据预处理阶段是机器学习中不可缺少的一环，它会使得数据更加有效的被模型或者评估器识别。下面我们来看一下sklearn中有哪些平时我们常用的函数：
				from sklearn import preprocessing
			2.1 数据归一化
　　			为了使得训练数据的标准化规则与测试数据的标准化规则同步，preprocessing中提供了很多Scaler：
				data = [[0, 0], [0, 0], [1, 1], [1, 1]]
				# 1. 基于mean和std的标准化
				scaler = preprocessing.StandardScaler().fit(train_data)
				scaler.transform(train_data)
				scaler.transform(test_data)

				# 2. 将每个特征值归一化到一个固定范围
				scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit(train_data)
				scaler.transform(train_data)
				scaler.transform(test_data)
				#feature_range: 定义归一化范围，注用（）括起来
			
			2.2 正则化（normalize）
　　			当你想要计算两个样本的相似度时必不可少的一个操作，就是正则化。其思想是：首先求出样本的p-范数，然后该样本的所有元素都要除以该范数，这样最终使得每个样本的范数都为1。
					>>> X = [[ 1., -1.,  2.],
					...      [ 2.,  0.,  0.],
					...      [ 0.,  1., -1.]]
					>>> X_normalized = preprocessing.normalize(X, norm='l2')

					>>> X_normalized                                      
					array([[ 0.40..., -0.40...,  0.81...],
						   [ 1.  ...,  0.  ...,  0.  ...],
						   [ 0.  ...,  0.70..., -0.70...]])
			
			2.3 one-hot编码
				one-hot编码是一种对离散特征值的编码方式，在LR模型中常用到，用于给线性模型增加非线性能力。
				data = [[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
				encoder = preprocessing.OneHotEncoder().fit(data)
				enc.transform(data).toarray()
		3. 数据集拆分
　　		在得到训练数据集时，通常我们经常会把训练数据集进一步拆分成训练集和验证集，这样有助于我们模型参数的选取。
			# 作用：将数据集划分为 训练集和测试集
			# 格式：train_test_split(*arrays, **options)
			from sklearn.mode_selection import train_test_split

			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
			"""
			参数
			---
			arrays：样本数组，包含特征向量和标签

			test_size：
			　　float-获得多大比重的测试样本 （默认：0.25）
			　　int - 获得多少个测试样本

			train_size: 同test_size

			random_state:
			　　int - 随机种子（种子固定，实验可复现）
			　　
			shuffle - 是否在分割之前对数据进行洗牌（默认True）

			返回
			---
			分割后的列表，长度=2*len(arrays), 
			(train-test split)
			"""
		
		4. 定义模型
			在这一步我们首先要分析自己数据的类型，搞清出你要用什么模型来做，然后我们就可以在sklearn中定义模型了。sklearn为所有模型提供了非常相似的接口，这样使得我们可以更加快速的熟悉所有模型的用法。在这之前我们先来看看模型的常用属性和功能：
				# 拟合模型
				model.fit(X_train, y_train)
				# 模型预测
				model.predict(X_test)

				# 获得这个模型的参数
				model.get_params()
				# 为模型进行打分
				model.score(data_X, data_y) # 线性回归：R square； 分类问题： acc
			4.1 线性回归
				from sklearn.linear_model import LinearRegression
				# 定义线性回归模型
				model = LinearRegression(fit_intercept=True, normalize=False, 
					copy_X=True, n_jobs=1)
				"""
				参数
				---
					fit_intercept：是否计算截距。False-模型没有截距
					normalize： 当fit_intercept设置为False时，该参数将被忽略。 如果为真，则回归前的回归系数X将通过减去平均值并除以l2-范数而归一化。
					 n_jobs：指定线程数
				"""
			4.2 逻辑回归LR
				from sklearn.linear_model import LogisticRegression
				# 定义逻辑回归模型
				model = LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0, 
					fit_intercept=True, intercept_scaling=1, class_weight=None, 
					random_state=None, solver=’liblinear’, max_iter=100, multi_class=’ovr’, 
					verbose=0, warm_start=False, n_jobs=1)

				"""参数
				---
					penalty：使用指定正则化项（默认：l2）
					dual: n_samples > n_features取False（默认）
					C：正则化强度的反，值越小正则化强度越大
					n_jobs: 指定线程数
					random_state：随机数生成器
					fit_intercept: 是否需要常量
				"""
			4.3 朴素贝叶斯算法NB
				from sklearn import naive_bayes
				model = naive_bayes.GaussianNB() # 高斯贝叶斯
				model = naive_bayes.MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
				model = naive_bayes.BernoulliNB(alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None)
				"""
				文本分类问题常用MultinomialNB
				参数
				---
					alpha：平滑参数
					fit_prior：是否要学习类的先验概率；false-使用统一的先验概率
					class_prior: 是否指定类的先验概率；若指定则不能根据参数调整
					binarize: 二值化的阈值，若为None，则假设输入由二进制向量组成
				"""
			 4.4 决策树DT
				from sklearn import tree 
				model = tree.DecisionTreeClassifier(criterion=’gini’, max_depth=None, 
					min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
					max_features=None, random_state=None, max_leaf_nodes=None, 
					min_impurity_decrease=0.0, min_impurity_split=None,
					 class_weight=None, presort=False)
				"""参数
				---
					criterion ：特征选择准则gini/entropy
					max_depth：树的最大深度，None-尽量下分
					min_samples_split：分裂内部节点，所需要的最小样本树
					min_samples_leaf：叶子节点所需要的最小样本数
					max_features: 寻找最优分割点时的最大特征数
					max_leaf_nodes：优先增长到最大叶子节点数
					min_impurity_decrease：如果这种分离导致杂质的减少大于或等于这个值，则节点将被拆分。
				"""
			4.5 支持向量机SVM
				from sklearn.svm import SVC
				model = SVC(C=1.0, kernel=’rbf’, gamma=’auto’)
				"""参数
				---
					C：误差项的惩罚参数C
					gamma: 核相关系数。浮点数，If gamma is ‘auto’ then 1/n_features will be used instead.
				"""
			4.6 k近邻算法KNN
				from sklearn import neighbors
				#定义kNN分类模型
				model = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1) # 分类
				model = neighbors.KNeighborsRegressor(n_neighbors=5, n_jobs=1) # 回归
				"""参数
				---
					n_neighbors： 使用邻居的数目
					n_jobs：并行任务数
				"""
			4.7 多层感知机（神经网络）
				from sklearn.neural_network import MLPClassifier
				# 定义多层感知机分类算法
				model = MLPClassifier(activation='relu', solver='adam', alpha=0.0001)
				"""参数
				---
					hidden_layer_sizes: 元祖
					activation：激活函数
					solver ：优化算法{‘lbfgs’, ‘sgd’, ‘adam’}
					alpha：L2惩罚(正则化项)参数。
				"""
		5. 模型评估与选择篇.
			5.1 交叉验证
				from sklearn.model_selection import cross_val_score
				cross_val_score(model, X, y=None, scoring=None, cv=None, n_jobs=1)
				"""参数
				---
					model：拟合数据的模型
					cv ： k-fold
					scoring: 打分参数-‘accuracy’、‘f1’、‘precision’、‘recall’ 、‘roc_auc’、'neg_log_loss'等等
				"""
			5.2 检验曲线
				from sklearn.model_selection import validation_curve
				train_score, test_score = validation_curve(model, X, y, param_name, param_range, cv=None, scoring=None, n_jobs=1)
				"""参数
				---
					model:用于fit和predict的对象
					X, y: 训练集的特征和标签
					param_name：将被改变的参数的名字
					param_range： 参数的改变范围
					cv：k-fold
				   
				返回值
				---
				   train_score: 训练集得分（array）
					test_score: 验证集得分（array）
				"""
				
		6. 保存模型
			6.1 保存为pickle文件
				import pickle
				# 保存模型
				with open('model.pickle', 'wb') as f:
					pickle.dump(model, f)

				# 读取模型
				with open('model.pickle', 'rb') as f:
					model = pickle.load(f)
				model.predict(X_test)
			6.2 sklearn自带方法joblib
				from sklearn.externals import joblib
				# 保存模型
				joblib.dump(model, 'model.pickle')

				#载入模型
				model = joblib.load('model.pickle')
				
				
		
		