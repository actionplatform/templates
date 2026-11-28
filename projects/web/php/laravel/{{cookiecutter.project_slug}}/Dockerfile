FROM composer:2 AS vendor
WORKDIR /app
COPY composer.json composer.lock ./
RUN composer install --no-dev --no-scripts --no-autoloader --prefer-dist --no-interaction

FROM php:{{ cookiecutter._php_version }}-cli-alpine
WORKDIR /app
COPY --from=vendor /usr/bin/composer /usr/bin/composer
COPY --from=vendor /app/vendor ./vendor
COPY . .
RUN composer dump-autoload --optimize --no-dev --no-interaction \
    && rm /usr/bin/composer \
    && adduser -D -u 10001 app \
    && chown -R app:app storage bootstrap/cache database
USER app
ENV APP_ENV=production \
    LOG_CHANNEL=stderr \
    PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "touch database/database.sqlite && php artisan migrate --force && exec php artisan serve --host=0.0.0.0 --port=${PORT}"]
