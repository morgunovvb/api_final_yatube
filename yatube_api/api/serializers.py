from rest_framework import serializers
from posts.models import Post, Group, Comment
from posts.models import Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('id', 'post', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('__all__')
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('user', 'following'),
                message=("Такая подписка уже существует и так")
            ),
        )

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя самого!')
        return data


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('__all__')
