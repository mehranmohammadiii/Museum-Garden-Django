from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator

class CustomMinimumLengthValidator(MinimumLengthValidator):
    
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(
                f"گذرواژه شما بسیار کوتاه است. حداقل باید {self.min_length} حرف داشته باشد.",
                code='password_too_short'
            )

    def get_help_text(self):
        return _(
            "رمز عبور شما می‌بایست حداقل از %(min_length)d حرف تشکیل شده باشد."
        ) % {'min_length': self.min_length}


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(
                _("این رمز عبور بیش از حد شبیه به نام کاربری می‌باشد."),
                code='password_too_similar'
            )

    def get_help_text(self):
        return _("گذرواژه شما نمی‌تواند بیش از حد شبیه به سایر اطلاعات شخصی شما باشد.")

class CustomCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(
                _("این رمز عبور بسیار رایج است و به راحتی قابل حدس زدن است."),
                code='password_too_common'
            )
            
    def get_help_text(self):
        return _("گذرواژه شما نمی‌تواند یک گذرواژه بسیار رایج باشد.")

class CustomNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(
                _("گذرواژه شما نمی‌تواند کاملاً از اعداد تشکیل شده باشد."),
                code='password_entirely_numeric'
            )

    def get_help_text(self):
        return _("گذرواژه شما نمی‌تواند کاملاً از اعداد تشکیل شده باشد.")