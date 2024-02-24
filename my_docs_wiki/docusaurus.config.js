const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

module.exports = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  url: 'https://localhost:3000',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  onBrokenAnchors: 'warn', // Note: 'onBrokenAnchors' might not be supported in all versions of Docusaurus
  favicon: 'img/favicon.ico',
  organizationName: 'outerbounds', // Your GitHub org/user name.
  projectName: 'nbdoc-docusaurus', // Your repo name.
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/outerbounds/nbdoc-docusaurus/tree/master/'
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/outerbounds/nbdoc-docusaurus/tree/master/'
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },  
    ],
  ],
  themes: ['@docusaurus/theme-mermaid'],
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'intro',
        },
        { to: '/blog', label: 'Blog', position: 'left' },
      ],
    },
    footer: {
      style: 'dark',
      // Define footer links here if necessary
    },
    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
    },
  },
  stylesheets: [
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap',
  ],

};
