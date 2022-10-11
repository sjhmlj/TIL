```django
{% load bootstrap5 %}

{% bootstrap_css %}
{% bootstrap_javascript %}
{% bootstrap_messages %}
<form action="{% url 'articles:create' %}" method="POST" class="form">
  {% csrf_token %}

  {% bootstrap_form form %}
  <input type="submit" class="btn btn-primary"> 
</form>
```

