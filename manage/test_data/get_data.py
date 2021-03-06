import  configparser, os
from enum import Enum, unique


class GetData(Enum):
    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = dir + "/date.ini"
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding='utf-8')
    project_name_t = cf.get("manage_project_info", "project_name_t")
    project_status = cf.get("manage_project_info", "project_status")
    project_category_t = cf.get("manage_project_info", "project_category_t")
    projectNewType_t = cf.get("manage_project_info", "projectNewType_t")
    financingMaturity_t = cf.get("manage_project_info", "financingMaturity_t")
    corporeType_t = cf.get("manage_project_info", "corporeType_t")
    amount_t = cf.get("manage_project_info", "amount_t")
    minBidAmount_t = cf.get("manage_project_info", "minBidAmount_t")
    repaymentCalcType_t = cf.get("manage_project_info", "repaymentCalcType_t")
    interestRatePercent_t = cf.get("manage_project_info", "interestRatePercent_t")
    displayInterestRate_t = cf.get("manage_project_info", "displayInterestRate_t")
    start_time_t = cf.get("manage_project_info", "start_time_t")
    end_time_t = cf.get("manage_project_info", "end_time_t")
    contractFullID_t = cf.get("manage_project_info", "contractFullID_t")
    contractType_t = cf.get("manage_project_info", "contractType_t")
    loanContract_t = cf.get("manage_project_info", "loanContract_t")
    address = cf.get("manage_project_info", "address")
    unicode = cf.get("manage_project_info", "unicode")
    bondManId = cf.get("manage_project_info", "bondManId")
    custRating_t = cf.get("manage_project_info", "custRating_t")
    userName_t = cf.get("manage_project_info", "userName_t")
    borrowerUserID = cf.get("manage_project_info", "borrowerUserID")
    borrowerUserRealName = cf.get("manage_project_info", "borrowerUserRealName")
    borrowerUserIDCard = cf.get("manage_project_info", "borrowerUserIDCard")
    borrowerPayType = cf.get("manage_project_info", "borrowerPayType")
    isRealBorrower = cf.get("manage_project_info", "isRealBorrower")
    realBorrowerName = cf.get("manage_project_info", "realBorrowerName")
    realBorrowerIdCard = cf.get("manage_project_info", "realBorrowerIdCard")
    area = cf.get("manage_project_info", "area")
    purpose_t = cf.get("manage_project_info", "purpose_t")
    houseGuaranteeInfo_t = cf.get("manage_project_info", "houseGuaranteeInfo_t")
    projectDescription_t = cf.get("manage_project_info", "projectDescription_t")
    repaymentSource_t = cf.get("manage_project_info", "repaymentSource_t")
    signAddr_t = cf.get("manage_project_info", "signAddr_t")
    custRating_t_bool = cf.get("manage_project_info", "custRating_t_bool")

    nativeProvince = cf.get("loanuser_info", "nativeProvince")
    companyEntryTime = cf.get("loanuser_info", "companyEntryTime")
    currentAddress = cf.get("loanuser_info", "currentAddress")
    ethnic = cf.get("loanuser_info", "ethnic")
    educationLevel = cf.get("loanuser_info", "educationLevel")
    maritalStatus = cf.get("loanuser_info", "maritalStatus")
    yearOfService = cf.get("loanuser_info", "yearOfService")
    quarters = cf.get("loanuser_info", "quarters")
    natureOfCompany = cf.get("loanuser_info", "natureOfCompany")
    industry = cf.get("loanuser_info", "industry")
    wage = cf.get("loanuser_info", "wage")
    province = cf.get("loanuser_info", "province")
    city = cf.get("loanuser_info", "city")
    houseRadiosid = cf.get("loanuser_info", "houseRadiosid")
    houseLoanRadios = cf.get("loanuser_info", "houseLoanRadios")
    carRadiosid = cf.get("loanuser_info", "carRadiosid")
    carLoanRadios = cf.get("loanuser_info", "carLoanRadios")



print(GetData['city'].value)