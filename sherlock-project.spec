# Packager: Paul Pfeister <rh-bugzilla@pfeister.dev> (GitHub @ppfeister)
%global source_ref master

Name:           sherlock-project
Version:        0.14.4
Release:        %autorelease
Summary:        Hunt down social media accounts by username across social networks

License:        MIT
URL:            https://github.com/sherlock-project/sherlock
Source:         %{url}/archive/%{source_ref}.tar.gz
# Switch to new Source URL after adoption of tagged releases

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Hunt down social media accounts by username across 400+ social networks and
websites. New targets are tested and implemented regularly.
}

%description %{_description}

%prep
%autosetup -n sherlock-%{source_ref}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sherlock sites result notify __init__ __main__

# Problematic
# sed -r -i '1{/^#!/d}' '%%{buildroot}%%{python3_sitelib}/*.py'

%check
# Tests fail when pwd isn't sherlock. Relative pathing need fix upstream.
cd sherlock
%{py3_test_envvars} %{python3} -m unittest tests.all --verbose
cd ..

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/sherlock
%{python3_sitelib}/resources
%pycached %{python3_sitelib}/tests/*.py

%changelog
* Tue May 14 2024 Paul Pfeister <rh-bugzilla@pfeister.dev> 0.14.4
- Initial package.
