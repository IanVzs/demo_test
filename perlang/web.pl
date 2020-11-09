#!/usr/bin/perl
use strict;
use warnings;

# Serve static files from document root with a directory index
# app.psgi
use Plack::App::Directory;
my $app = Plack::App::Directory->new({
        root => "/path/to/htdocs"
})->to_app;
