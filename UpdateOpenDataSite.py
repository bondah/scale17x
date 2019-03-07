import fileinput, os, distutils.dir_util

devFolder = 'I:\IT\Software Solutions\Open Data\Demo Site\opendata'
siteFolder1 = '//cmsapp01/Apache Software Foundation/webapps/ROOT/opendata'
siteFolder2 = '//cmsapp02/Apache Software Foundation/webapps/ROOT/opendata'

# update site
app_path = os.path.join('C:\\', 'Ruby200-x64', 'bin')
os.environ["PATH"] += os.pathsep + app_path
os.chdir(devFolder)
os.system('bundle exec jekyll build');
distutils.dir_util.copy_tree(devFolder +'\_site', siteFolder1)
distutils.dir_util.copy_tree(devFolder +'\_site', siteFolder2)
