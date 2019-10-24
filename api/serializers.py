from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name']


class ItemSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'api-item-detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'item_id'
		)
	added_by = UserSerializer()
	favorited_by = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'detail', 'added_by', 'favorited_by']

	def get_favorited_by(self, obj):
		favorites = FavoriteItem.objects.filter(item=obj)
		return len(favorites)


class ItemDetailSerializer(serializers.ModelSerializer):
	favorited_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'favorited_by']

	def get_favorited_by(self, obj):
		favorites = FavoriteItem.objects.filter(item=obj)
		favorite_list=[]
		for favorite in favorites:
			#favorite_list.append(favorite.user)
			favorite_list.append(UserSerializer(favorite.user).data)
			#print(favorite_list)
			# return favorite_list.data

		return favorite_list


		# return UserSerializer(favorites).data
		# queryset.values_list()