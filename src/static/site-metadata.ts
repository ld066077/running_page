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
  siteTitle: 'Running',
  siteUrl: 'https://run.imyxl.com',
  logo: '',
  description: 'Personal site and blog',
  navLinks: [
    {
      name: 'Blog',
      url: 'https://imyxl.com',
    }
  ],
};

export default data;
