interface ISiteMetadataResult {
  siteTitle: string;
  siteUrl: string;
  description: string;
  logo: string;
  navLinks: {
    name: string;
    url: string;
  }[];
}

const data: ISiteMetadataResult = {
  siteTitle: 'imyxl的跑步记录',
  siteUrl: 'https://running-lyart.vercel.app',
  logo: '',
  description: 'Personal site and blog',
  navLinks: [
    {
      name: '我的博客',
      url: 'https://imyxl.com',
    },
    {
      name: '我的github仓库',
      url: 'https://github.com/ld066077',
    }
  ],
};

export default data;
