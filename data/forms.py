from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    first_name = wtforms.StringField("Введіть своє ім'я")
    last_name = wtforms.StringField("Введіть своє призвіще")
    email = wtforms.EmailField("Email", validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Введіть пароль", validators=[wtforms.validators.length(8)])
    submit = wtforms.SubmitField("Зареєструватись")


class LoginForm(FlaskForm):
    email = wtforms.EmailField("Email", validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(8)])
    submit = wtforms.SubmitField("Увійти")